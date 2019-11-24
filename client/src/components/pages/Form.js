
import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addRestaurant } from "../../actions/restaurants";
import restaurants from "../../reducers/restaurants";

export class Form extends Component {
  state = {
    room_address: "",
    room_zipcode: "",
    room_city: "",
    room_title: "",
    room_is_active: "",
    room_is_validated: "",
    informations: "", 
    longitude: "",
    latitude: ""
  };

  static propTypes = {
    addRestaurant: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {

    e.preventDefault();

    const { 
        room_address, room_zipcode, room_city, room_title, 
        room_is_active, room_is_validated, informations, 
        longitude, latitude
    } = this.state;

    const lead = { 
        room_address, room_zipcode, room_city, room_title, 
        room_is_active, room_is_validated, informations, 
        longitude, latitude
    };

    this.props.addRestaurant(restaurants);

    this.setState({
        room_address: "",
        room_zipcode: "",
        room_city: "",
        room_title: "",
        room_is_active: "",
        room_is_validated: "",
        informations: "", 
        longitude: "",
        latitude: ""
    });
  };

  render() {
    const { room_address, room_zipcode, room_city, room_title, 
        room_is_active, room_is_validated, informations, 
        longitude, latitude } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Restaurant</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>room_address</label>
            <input
              className="form-control"
              type="text"
              name="room_address"
              onChange={this.onChange}
              value={room_address}
            />
          </div>
          <div className="form-group">
            <label>room_zipcode</label>
            <input
              className="form-control"
              type="text"
              name="room_zipcode"
              onChange={this.onChange}
              value={room_zipcode}
            />
          </div>
          <div className="form-group">
            <label>room_city</label>
            <textarea
              className="form-control"
              type="text"
              name="room_city"
              onChange={this.onChange}
              value={room_city}
            />
          </div>
          <div className="form-group">
            <label>room_title</label>
            <textarea
              className="form-control"
              type="text"
              name="room_title"
              onChange={this.onChange}
              value={room_title}
            />
          </div>
          <div className="form-group">
            <label>room_is_active</label>
            <textarea
              className="form-control"
              type="checkbox"
              name="room_is_active"
              onChange={this.onChange}
              value={room_is_active}
            />
          </div>
          <div className="form-group">
            <label>room_is_validated</label>
            <textarea
              className="form-control"
              type="checkbox"
              name="room_is_validated"
              onChange={this.onChange}
              value={room_is_validated}
            />
          </div>
          <div className="form-group">
            <label>informations</label>
            <textarea
              className="form-control"
              type="text"
              name="informations"
              onChange={this.onChange}
              value={informations}
            />
          </div>
          <div className="form-group">
            <label>longitude</label>
            <textarea
              className="form-control"
              type="text"
              name="longitude"
              onChange={this.onChange}
              value={longitude}
            />
          </div>
          <div className="form-group">
            <label>latitude</label>
            <textarea
              className="form-control"
              type="text"
              name="latitude"
              onChange={this.onChange}
              value={latitude}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(
  null,
  { addRestaurant }
)(Form);