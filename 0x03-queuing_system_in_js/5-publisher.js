import redis from 'redis';

const publisher = redis.createClient();

publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

publisher.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function publicMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school', message);
    }, time);
}

publicMessage('Holberton Student #1 starts course', 100);
publicMessage('Holberton Student #2 starts course', 200);
publicMessage('KILL_SERVER', 300);
publicMessage('Holberton Student #3 starts course', 400);
