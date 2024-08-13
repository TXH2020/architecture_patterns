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
