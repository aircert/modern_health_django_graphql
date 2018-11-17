import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Grid from "./Grid";
import { Container, Row, Col} from 'reactstrap';

const App = () => (
	<div>
		<Container>
			<Row> 
				<Col md="12"> 
					<DataProvider endpoint="graphql" 
		                render={data => <Grid data={data} />} />
				</Col>
			</Row>
		  	
		</Container>
	</div>
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;