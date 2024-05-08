import kue from 'kue';

const pushNotificationQueue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = pushNotificationQueue.create('push_notification_code', jobData);

// job creation
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// handle job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

job.save();
