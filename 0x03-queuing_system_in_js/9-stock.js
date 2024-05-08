import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();
const getAsyncStockById = promisify(redisClient.get).bind(redisClient);

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const PORT = 1245;
const app = express();
app.use(express.json());

const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.find((product) => product.itemId === id);
}

// stores product in redis
function reserveStockById(itemId, stock) {
  redisClient.set(itemId, JSON.stringify(stock));
}

// retrieves product from redis
async function getCurrentReservedStockById(itemId) {
  const item = await getAsyncStockById(itemId);
  return JSON.parse(item);
}

app.get('/list_products', (req, res) => {
  res.status(200).json(listProducts);
});

app.get('/list_products/:itemId([0-9]+)', async (req, res) => {
  const { itemId } = req.params;
  const product = await getCurrentReservedStockById(itemId);

  if (!product) return res.status(404).json({ status: 'Product not found' });

  return res.status(200).json({
    ...product,
    currentQuantity: product.initialAvailableQuantity,
  });
});

app.get('/reserve_product/:itemId([0-9]+)', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(+itemId);

  if (!product) return res.status(404).json({ status: 'Product not found' });

  if (product.initialAvailableQuantity < 1) {
    return res.json({ status: 'Not enough stock available', itemId: 1 });
  }
  reserveStockById(product.itemId, product);
  return res.json({ status: 'Reservation confirmed', itemId: 1 });
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});
