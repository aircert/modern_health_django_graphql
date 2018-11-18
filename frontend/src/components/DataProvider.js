import React, { Component } from "react";
import PropTypes from "prop-types";
import axios from 'axios';

class DataProvider extends Component {
  propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  };
  state = {
      data: [],
      loaded: false,
      placeholder: "Loading..."
    };
  componentDidMount() {
    axios({
      url: this.props.endpoint,
      method: 'post',
      data: {
        query: `
          query ProgramsQuery {
            allPrograms {
              id
              name
              description
              progress
              image
              weeks {
                name
                pages {
                  name
                  complete
                  audio
                }
              }
            }
          }
        `
      }
    }).then((result) => {
      console.log(result.data)
      this.setState({ data: result.data.data.allPrograms, loaded: true })
    });

    // fetch(this.props.endpoint)
    //   .then(response => {
    //     if (response.status !== 200) {
    //       return this.setState({ placeholder: "Something went wrong" });
    //     }
    //     return response.json();
    //   })
    //   .then(data => );
  }
  render() {
    const { data, loaded, placeholder } = this.state;
    return loaded ? this.props.render(data) : <p>{placeholder}</p>;
  }
}
export default DataProvider;