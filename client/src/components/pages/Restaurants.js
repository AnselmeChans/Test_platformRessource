import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getRestaurants, deleteRestaurant } from "../../actions/restaurants";

export class Restaurants extends Component {
  static propTypes = {
    restaurants: PropTypes.array.isRequired,
    getRestaurants: PropTypes.func.isRequired,
    deleteRestaurant: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getRestaurants();
  }

  render() {
    return (
      <Fragment>
        <h2>RESTAURANTS</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Room address</th>
              <th>Room zipcode</th>
              <th>City</th>
              <th>Title</th>
              <th>Informations</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.restaurants.map(restaurant => (
              <tr key={restaurant.id}>
                <td>{restaurant.id}</td>
                <td>{restaurant.room_address}</td>
                <td>{restaurant.room_zipcode}</td>
                <td>{restaurant.room_city}</td>
                <td>{restaurant.room_title}</td>
                <td>{restaurant.informations}</td>
                <td>
                  <button
                    onClick={this.props.deleteRestaurant.bind(this, restaurant.id)}
                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  restaurants: state.restaurants.restaurant
});

export default connect(
  mapStateToProps,
  { getRestaurants, deleteRestaurant }
)(Restaurants);