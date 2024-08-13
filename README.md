# Architecture Patterns

1. Monolithic
2. Microservices
3. Client-server: Amazon etc. All nodes communicate to/from a single node called "server". Hence these nodes are called "clients". The architecture is "centralized". Think of pinging google.
4. Peer-to-Peer(P2): BitTorrent etc. Nodes are called "Peers" because:
    1. They can act as both clients and servers.
    2. They generally communicate over "overlay" networks. These are abstractions i.e., virtual/logical networks that run on top of actual physical networks. Hence, at application level, the nodes can directly communicate with each other.

       Thus, the architecture is "decentralized". Think of pinging one computer from another and vice versa.
5. Service Oriented Architecture(SOA): Due to lots of industry jargon and misconceptions, SOA is tightly associated with the Enterprise Service Bus(ESB) which integrates disparate components. Failure of the ESB is the failure of the whole application.

   This [link](https://www.ibm.com/topics/esb) provides a description of the ESB and also provides a link to a 2 part article on SOA. This article further introduces two other architectural patterns: point-to-point architecture and hub-spoke architecture.

   To summarize, all the three mentioned architectures(point-to-point, hub-spoke and SOA) can be considered as primitive forms of a component based architecture, while Microservices is a modern component based architecture.
   
6. Event Driven Architecture: Here the nodes are of two types: producers and consumers, with respect to events. This pattern is different from competing consumers pattern because in CC pattern, every event is passed only to a single consumer unlike EDA where all consumers get every message. EDA can be implemented using Pub-Sub(once you read, you cant read again) or an event stream(a streaming log. you can replay messages, but you are responsible for pointing/offsets). Best examples are applications involving Google Cloud pub sub and Kafka. Remember Kafka Console Producer and Consumer.
   
   [EDA](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven)
7. N-Tier Architecture(Layered): Consider the application in this link as an example: [link](https://github.com/TXH2020/OtherProjects/tree/main/spring)
   
   [N-Tier](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier)

8. Serverless Architecture: Instead of worrying about how to provision resources to deliver a solution, use a managed service and focus only on the functionality or "function", i.e., the end service provided to the user.

   [Serverless](https://www.spiceworks.com/tech/devops/articles/what-is-serverless/amp/#_003)

9. Lambda Architecture:
    
    [About Lambda Architecture](https://www.cazton.com/consulting/enterprise/lambda-architecture)

   [Lambda Architecture Example](https://github.com/apssouza22/big-data-pipeline-lambda-arch)
10. Kappa Architecture: It is a simpler alternative to the lambda architecture, where the streaming engine itself is used to perform batch transactions, eliminating the need for separate batch processing engines.
    [Kappa architecture](https://hazelcast.com/glossary/kappa-architecture/)

11. Space Based Architecture: This and some other architectures are designed keeping scalability in mind. Essentially, we have a set of independent "processing units" which can be considered as various services. For instance, consider this example from monolithic architecture. Suppose we want to scale out our hello and hi services. Let it be that they depend on a database of names, which, even though can be scaled out, still becomes a bottleneck and also difficult to maintain consistency across all db instances. Instead, let all instances of hello and hi services be connected to a shared, distributed cache. This eliminates the db bottleneck, simplifies the code and makes it easier to scale due to in memory transactions. The obvious drawback is that we cannot store large amounts of data in a memory store.

    [SBA](https://www.linkedin.com/pulse/software-architecture-space-based-pattern-shanoj-kumar-v-5nknc)
    
13. Shared Everything, Shared nothing and shared disk/memory: The terms appear self explanatory. In shared everything, both memory and disk is shared among all nodes, for maximizing resource utilisation. In shared disk architecture, we cannot partition the data(similarly for shared memory). In shared nothing architecture, all nodes are independent, and a single node caters to each request. This eliminates contention.

    [SNA](https://en.m.wikipedia.org/wiki/Shared-nothing_architecture)

14. Cloud Native Architecture: Consider this to be a microservice approach developed and deployed on the cloud.
    
    [Cloud Native](https://aws.amazon.com/what-is/cloud-native/)

These were some of the major architectural patterns. Terminologies may vary from place to place. According to me, these patterns are vast, covering almost all aspects of software architecture. Others can be called design patterns which are closer to coding i.e, solve specific problems. For example, MVC, Pipelines(pipe and filter) etc. There are too many design patterns like this. Once again design patterns in the strict sense refer to a set of distinct patterns in software design: adapter, factory, pubsub etc. Microsoft has published a long catalog of cloud design patterns: [catalog](https://learn.microsoft.com/en-us/azure/architecture/patterns/)
