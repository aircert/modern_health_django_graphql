# modern_health_django_graphql

All you gotta do is `https://github.com/aircert/modern_health_django_graphql.git` `cd modern_health_django_graphql` then `make`

### Access GraphQL Explorer
	- Navigate to http://localhost:8000/graphiql
	- Query All Programs 
	```
	query {
	  allPrograms {
	    id
	    name
	    description
	    progress
	    weeks {
	      id
	      name
	      pages {
	        id 
	        name
	        complete
	      }
	    }
	  }
	}
	```

### Check Frontend 
	- Navigate to http://localhost:8000