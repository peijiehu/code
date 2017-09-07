---
layout: post
title: Some Notes on Kafka
excerpt: ''
categories: [note]
date:   2017-09-06 22:00:00
comments: true
---

## Some Notes on Kafka

A common use case of Kafka - database change stream, requires understanding of stream-table duality. DB usually has transaction logs which can be used by a fetcher process to publish row based changes to streaming service like Kafka.

Although with the new Kafka Streams introduced in 2016, Kafka can replace a lot of what DB has and become more than DB because DB can only store states for some point of time while data in Kafka represent states at different times and how they change over time.

In a Micro-Service system, one bonus from Kafka or other message bus: it would reduce the inter-service connection complexity from n^2 to n, the decoupling reduces both the complexity of the system and network bandwidth.

### When Not To Use Kafka

The fact that the result of an action is not returned immediately can also increase the complexity of system and user interface design and in some scenarios it does not even make logical sense for a subset of a system to function in an asynchronous manner. Take the Back in Stock Notifier for example, and its relationship with the Subscriber Manager; it is impossible for the notifier to function without information about the subscribers that it should be notifying, and therefore a synchronous REST call makes sense in this case. This differs from the email sending task, as there is no need for emails to be sent immediately.

### Kafka in production

#### Disk
SSDs are not necessary, there's not much performance benefits mostly because Kafka writes to disk are asynchronous.
Disk Allocation:
```
avg msg size * num of msg per sec * retention period * replication factor
msg = "{'status': 'success', 'meta': 'some meta data'}"
sys.getsizeof(msg) * 10 msg/s * 3600*24*7 s * 3
```

#### Memory
A back-of-the-envelope estimate of memory needs by assuming you want to be able to buffer for 30 seconds and compute your memory need as write_throughput * 30. You can get the estimated write_throughput by looking at network monitor of the instace that hosts Kafka.

#### Replication
Replicating to at least 3 replicas is critical—because a single replica will lose the data that has not been sync’d to disk, if it crashes.

For mission critical data:
```
acks=all
replication.factor=3
min.insync.replicas=2
unclean.leader.election.enable=false
```

#### Zookeeper
Zookeeper is used by Kafka as a leader election as well as metadata storage about Kafka topics, brokers. Kafka broker topic-partition leadership is managed by zookeeper watchers on /broker/ids/{brokerId} nodes. Also Kafka controller which manages the entire cluster is done by zookeeper itself.

In short, zookeeper availability is critical to Kafka. You can definitely run a kafka cluster with single zookeeper. But it's highly recommended to run a zookeeper quorum of 3 or 5 servers in production. Anything less than you will run into issues, essentially by running single zookeeper instance you are setting up for single point of failure here.

Also recommended to not to have zookeeper and kafka on the same machines, both are disk heavy. Kafka performance comes from having sole access to disk and ability to use page cache on that disk.

Recommended minimum fault tolerant cluster would be 3 Kafka brokers and 3 zookeeper nodes with replication factor = 3 on all topics.

### Misc
Centralized cluster and topic management with web interface - Kafka Manager
https://github.com/yahoo/kafka-manager

Options to persist data from Kafka
https://www.mongodb.com/blog/post/mongodb-and-data-streaming-implementing-a-mongodb-kafka-consumer
https://kafka.apache.org/documentation/#connect

### Referrences
https://www.slideshare.net/ConfluentInc/streaming-in-practice-putting-apache-kafka-in-production
http://docs.confluent.io/1.0/kafka/deployment.html
https://www.confluent.io/blog/hands-free-kafka-replication-a-lesson-in-operational-simplicity/
http://blog.cloudera.com/blog/2015/07/deploying-apache-kafka-a-practical-faq/
