import React, { Component, Fragment } from "react";

import Form from "./Form";
import Restaurant from "./Restaurants";
import CardsRest from "../layouts/CardsRessources";


export default class Home extends Component {
    render() {
        return (
            <Fragment>
                <h1> Welcom to the listing of room restaurant </h1>
                <CardsRest></CardsRest>
      
            </Fragment>
        )
    }
}



