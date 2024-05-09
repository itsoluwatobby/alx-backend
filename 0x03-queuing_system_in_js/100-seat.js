import { promisify } from 'util';
import { createClient } from 'redis';
import kue from 'kue';
import express from 'express';

const PORT = 1245;

const app = express();
app.use(express.json());
const queue = kue.createQueue();

const redisClient = createClient();
const getAsyncCurrentSeats = promisify(redisClient.get).bind(redisClient);

let reservationEnabled = true;

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function reserveSeat(number) {
  redisClient.set('available_seats', number);
}
// when launched, initialized "available_seats" with 50
reserveSeat(50);

async function getCurrentAvailableSeats() {
  const val = await getAsyncCurrentSeats('available_seats');
  if (val <= 0) reservationEnabled = false;
  return val;
}

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({numberOfAvailableSeats:availableSeats});
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) return res.json({status:"Reservation are blocked"});
  const job = queue.create('reserve_seat');
  job.on('enqueue', () => {
    console.log(`Seat reservation job created: ${job.id}`);
  });
  job.on('completed', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
  job.save();
  return res.json({status:'Reservation in process'});
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});
