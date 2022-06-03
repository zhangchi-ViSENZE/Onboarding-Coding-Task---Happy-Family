# Onboard - happy family - design document

## Context
The wife said: "Please go to the store and buy a carton of milk and if they have eggs, get 12." The husband came back with 12 cartons of milk. The wife said: "why in the hell did you buy 12 cartons of milk." The husband responded: "They had eggs."

## User Story
As a husband who don't like go shopping, when my wife asks me to go and buy something
I would like to check if the product available or not before I go to the store
so that I don't waste my time and find the product everywhere and I buy the product correctly.  

## Acceptance Criteria
Given a store that sells milk cartons and eggs.
When husband makes a purchase.
Then he should get 1 milk carton if eggs sold out.
Then he should get 1 milk carton and 12 eggs if eggs are on stock.

## Design
### Architecture
provide a class/component diagram to illustrate the architecture. Set the scope of development

### Workflow
husband check the product stock remotely
if it's available,  buy the product.

### API specification
| Method | Name | Description | Param | Response
| --- | --- | --- | --- | ---|
| GET | /store/hasmilk | queries store for milk availability | - | quantity of milk available |
| GET | /store/haseggs | queries store for eggs availability | - | quantity of eggs available |
| POST | /store/buymilk | buys milk from store | quantity | quantity of milk bought |
| POST | /store/hasmilk | buys eggs from store | quantity | quantity of milk bought |

#### **Constraints**
the API server must be up, and the service must be started

#### **Error message**
| Description | Response |
| --- | ---- |
| Quantity is not a positive integer | { “error_code”: 101, “error_msg”: “Parameter must be a positive integer.” } |
| Quantity is exceed the current availability | { “error_code”: 400, “error_msg”: “Parameter must be smaller.” } |
| Product is not in the database | { “error_code”: 404, “error_msg”: “Product not found and Unsuccessful Purchase.” } |

## Implementation
Component impacted
N/A
<Component A>
N/A
<Component B>
N/A

## Testing
 
## Execution
 
## References