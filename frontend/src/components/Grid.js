import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import { Col } from 'reactstrap';

const Grid = ({ data }) =>
  !data.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      {data.map(el => (
        <div key={el.id} className="program">
          <Col md="12">
            <h5>
              {el.name} ({el.weeks.length} weeks)
            </h5>
            <h6>
              {el.description}
            </h6>
            <div>
              {el.weeks.map(week => (
                <div>
                  <p key={week.id}>
                    {week.name} ({week.pages.length} pages)
                  </p>
                </div>
              ))}
            </div>
          </Col>
        </div>
      ))}
    </div>
  );

Table.propTypes = {
  data: PropTypes.array.isRequired
};

export default Table;