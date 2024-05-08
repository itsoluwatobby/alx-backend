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

async function getCurrentAvailableSeats() {
  const val = await getAsyncCurrentSeats('available_seats');
  if (val === 0) reservationEnabled = false;
}
// when launched, initialized "available_seats" with 50
reserveSeat(50);

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});
