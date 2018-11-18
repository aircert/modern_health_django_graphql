# modern_health_django_graphql

All you gotta do is `https://github.com/aircert/modern_health_django_graphql.git` `cd modern_health_django_graphql` then `make`

### Access GraphQL Explorer
[link http://localhost:8000/graphiql](http://localhost:8000/graphql?query=%23%20Create%20page%0A%0A%23%20mutation%20%7B%0A%23%20%20%20pageCreate(newPage%3A%20%7B%0A%23%20%20%20%20%20name%3A%20%22Page%206%22%2C%20%0A%23%20%20%20%20%20video%3A%20%22http%3A%2F%2Fgoogle.com%2Fvideo%22%2C%0A%23%20%20%20%09audio%3A%20%22http%3A%2F%2Fgoogle.com%2Faudio%22%2C%0A%23%20%20%20%20%20form%3A%20%22http%3A%2F%2Fgoogle.com%2Fform%22%2C%0A%23%20%20%20%20%20question%3A%20%22http%3A%2F%2Fgoogle.com%2Fquestion%22%2C%0A%23%20%20%20%20%20article%3A%20%22http%3A%2F%2Fgoogle.com%2Farticle%22%0A%23%20%20%20%7D)%20%7B%0A%23%20%20%20%20%20page%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Create%20Week%0A%23%20mutation%20%7B%0A%23%20%20%20weekCreate(newWeek%3A%20%7B%0A%23%20%20%20%20%20pages%3A%20%5B6%2C%205%5D%2C%0A%23%20%20%20%20%20name%3A%20%22Week%204%22%0A%23%20%20%20%7D)%20%7B%0A%23%20%20%20%09week%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20pages%20%7B%0A%23%20%20%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Delete%20Program%0A%23%20mutation%20%7B%0A%23%20%20%20programDelete(id%3A%202)%20%7B%0A%23%20%20%20%20%20program%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Create%20Program%0A%23%20mutation%20%7B%0A%23%20%20%20programCreate(newProgram%3A%20%7B%0A%23%20%20%20%20%20name%3A%20%22Mindful%20Communication%22%2C%0A%23%20%20%20%20%20description%3A%20%22Minfully%20communicate%20with%20coworkers%22%2C%0A%23%20%20%20%20%20weeks%3A%20%5B3%2C4%5D%2C%0A%23%20%20%20%20%20progress%3A%200%0A%23%20%20%20%7D)%20%7B%0A%23%20%20%20%20%20program%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20description%0A%23%20%20%20%20%20%20%20progress%0A%23%20%20%20%20%20%20%20image%0A%23%20%20%20%20%20%20%20weeks%20%7B%0A%23%20%20%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20%20%20pages%20%7B%0A%23%20%20%20%20%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%20%20errors%20%7B%0A%23%20%20%20%20%20%20%20messages%0A%23%20%20%20%20%20%20%20field%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Get%20All%20Weeks%20%0A%23%20query%20%7B%0A%23%20%20%20allWeeks%20%7B%0A%23%20%20%20%20%20id%0A%23%20%20%20%20%20name%0A%23%20%20%20%20%20pages%20%7B%0A%23%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Get%20all%20pages%0A%0A%23%20query%20%7B%0A%23%20%20%20allPages%20%7B%0A%23%20%20%20%20%20id%0A%23%20%20%20%20%20name%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%0A%23%20Get%20all%20programs%2C%20weeks%2C%20and%20pages%20for%20each%0Aquery%20%7B%0A%20%20allPrograms%20%7B%0A%20%20%20%20id%0A%20%20%20%20name%0A%20%20%20%20description%0A%20%20%20%20progress%0A%20%20%20%20image%0A%20%20%20%20weeks%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20pages%20%7B%0A%20%20%20%20%20%20%20%20id%20%0A%20%20%20%20%20%20%20%20name%0A%20%20%20%20%20%20%20%20complete%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0A%23%20Update%20a%20program%20by%20weeks%20%0A%23%20mutation%20%7B%0A%23%20%20%20programUpdate(newProgram%3A%20%7Bid%3A%202%2C%20weeks%3A%20%5B1%2C2%2C3%2C4%5D%7D)%20%7B%0A%23%20%20%20%20%20program%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20weeks%20%7B%0A%23%20%20%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Update%20a%20pages%20progress%20to%20complete%0A%23%20mutation%20%7B%0A%23%20%20%20pageUpdate(newPage%3A%20%7Bid%3A%201%2C%20complete%3A%20true%7D)%20%7B%0A%23%20%20%20%20%20page%20%7B%0A%23%20%20%20%20%20%09id%0A%23%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%20%20dateModified%0A%23%20%20%20%20%20%20%20dateCreated%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D)
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