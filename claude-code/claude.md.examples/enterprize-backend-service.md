# Project: Payment Processing Microservice

## Service Architecture
- **Framework**: Spring Boot 3.1 with Java 17
- **Database**: PostgreSQL with JPA/Hibernate
- **Security**: OAuth 2.0 with JWT tokens
- **Documentation**: OpenAPI 3.0 specifications
- **Deployment**: Docker containers with Kubernetes

## Development Workflow
1. Create feature branch: `backend-[ticket-number]-[description]`
2. Write integration tests for all new endpoints
3. Update OpenAPI documentation for API changes
4. Run full test suite: `./gradlew test integrationTest`
5. Ensure Docker build succeeds: `docker build -t payment-service .`
6. Commit with ticket reference: `feat: [TICKET-123] Add payment validation`

## Code Standards
- Follow Google Java Style Guide
- Use Spring Boot conventions for package structure
- All REST endpoints must have comprehensive validation
- Use DTOs for all external API contracts
- Implement proper exception handling with @ControllerAdvice

## Package Structure
- `controller`: REST endpoints and request/response handling
- `service`: Business logic and transaction management  
- `repository`: Data access layer with JPA repositories
- `config`: Configuration classes and beans
- `dto`: Data Transfer Objects for API contracts
- `entity`: JPA entities for database mapping
- `exception`: Custom exceptions and error handling

## Security Requirements
- All endpoints require authentication except health checks
- Validate all inputs with Bean Validation annotations
- Use parameterized queries to prevent SQL injection
- Log security events for audit trail
- Never expose internal entity models in API responses

## Quality Gates
- Minimum 85% test coverage (unit + integration)
- All dependencies must be up-to-date and vulnerability-free
- SonarQube quality gate must pass
- All database migrations must be reversible
- Performance tests must complete under 200ms for standard operations

## Monitoring and Logging
- Use structured logging with JSON format
- Include correlation IDs for request tracing
- Monitor key metrics: response time, error rate, throughput
- Implement health checks for Kubernetes readiness/liveness probes