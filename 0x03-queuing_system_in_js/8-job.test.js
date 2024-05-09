import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient() }, testMode: true });
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.shutdown(1000, (err) => {
            if (err) throw err;
        });
    });

    it('display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
    });

    it('create two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '415351870',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '415351871',
                message: 'This is the code 4562 to verify your account'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
    });
});
