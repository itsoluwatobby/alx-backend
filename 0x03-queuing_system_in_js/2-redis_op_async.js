import { createClient, print } from 'redis';
import { promisify } from 'util';

const redisClient = createClient();

const getAsync = promisify(redisClient.get).bind(redisClient);

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
