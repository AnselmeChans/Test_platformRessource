import { GET_RESTAURANTS, DELETE_RESTAURANTS, ADD_RESTAURANTS, CLEAR_RESTAURANTS } from "../actions/types.js";

const initialState = {
  restaurants: []
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_RESTAURANTS:
      return {
        ...state,
        restaurants: action.payload
      };
    case DELETE_RESTAURANTS:
      return {
        ...state,
        restaurants: state.leads.filter(lead => lead.id !== action.payload)
      };
    case ADD_RESTAURANTS:
      return {
        ...state,
        restaurants: [...state.leads, action.payload]
      };
    case CLEAR_RESTAURANTS:
      return {
        ...state,
        restaurants: []
      };
    default:
      return state;
  }
}