import React, { Component } from 'react';
import { InfoConsumer } from '../context';


export default class Ressources extends Component {
    render() {
        return (
            <InfoConsumer>
                {data => {
                    return(
                    <h2> {data} </h2>
                    );
                }}
            </InfoConsumer>
        );
    }
}
