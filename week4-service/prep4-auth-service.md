## Security concepts

Review security concepts:
* https://www.computer.org/resources/software-security
    - optional: SWEBOK ch.13
* https://www.ibm.com/think/topics/authentication

Some good stuff here:
- https://microservices.io/post/architecture/2025/04/25/microservices-authn-authz-part-1-introduction.html

## Key concepts

* Our service vs a "real" service
    - in our context (controller-service-repository in a monolith), service just means "the thing that does the business logic." (handling a bounded context - e.g. our User service that handles user management and authentication)
    - in most professional contexts, Service means someting like "a discrete unit of functionality that is independently deployed and communicates with other components via HTTP."

* Here's our plan over the next several weeks:
    * First (this week), we'll be implementing the capabilities for authentication and authorization in our UserService (python class).
        - authentication attempts will have to go through the service
        - any requests to CRUD users will need to be authorized
        - passwords will be hashed in the UserService.
    * Next few weeks, we will build an app (controller) with login capabilities.  The app will handle sessions and such, so that users can be authenticated over multiple requests.
    * Later, we will build an api (another controller) with authentication and authorization via tokens that are passed with HTTP requests.

* So, for now, what you need to know about:
    
    * basic security concepts
    * general concepts / approach for services and CSR pattern
        - service as a unit of functionality / bounded context.
        - (i.e., any access to the repository has to go through the service)
    * implementing password hashing for user creation and authentication
    * authorization by passing a User object as a "requester" parameter.
