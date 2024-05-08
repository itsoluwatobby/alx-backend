import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('ready', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (err, reply) => {
    if (!err) console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
