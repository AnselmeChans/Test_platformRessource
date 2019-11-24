import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_RESTAURANTS, DELETE_RESTAURANTS, ADD_RESTAURANTS } from "./types";

// GET Restaurant
export const getRestaurants = () => (dispatch, getState) => {
  axios
    .get("/api/restaurant/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_RESTAURANTS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// DELETE Restaurant
export const deleteRestaurant = id => (dispatch, getState) => {
  axios
    .delete(`/api/restaurant/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ deleteRestaurant: "Restaurant Deleted" }));
      dispatch({
        type: DELETE_RESTAURANTS,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

// ADD Restaurant
export const addRestaurant = restaurant => (dispatch, getState) => {
  axios
    .post("/api/restaurant/", restaurant, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addRestaurant: "Restaurant added" }));
      dispatch({
        type: ADD_RESTAURANTS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};