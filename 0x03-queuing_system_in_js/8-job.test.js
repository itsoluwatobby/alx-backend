import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after tests
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create push notifications jobs', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'This is the first message' },
      { phoneNumber: '9876543210', message: 'This is the second message' },
    ];
    createPushNotificationsJobs(jobs, queue);

    // Assert that jobs are correctly added to the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Assert job properties
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('1234567890');
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('9876543210');
    expect(queue.testMode.jobs[0].data.message).to.equal('This is the first message');
    expect(queue.testMode.jobs[1].data.message).to.equal('This is the second message');
  });

  // Add more test cases as needed
  it('display a error message if jobs is not an array', () => {
    const jobs = {
      phoneNumber: '9876543210',
      message: 'This is the second message',
    };
    expect(() => createPushNotificationsJobs(jobs, queue)).throw('Jobs is not an array');
  });
});
