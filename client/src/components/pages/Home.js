import React, { Component, Fragment } from "react";

import Form from "./Form";
import Restaurant from "./Restaurants";


export default class Home extends Component {
    render() {
        return (
            <Fragment>
                <Form />
                <Restaurant />
            </Fragment>
        )
    }
}



