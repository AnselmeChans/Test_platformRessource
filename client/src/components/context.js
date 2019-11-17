import React, { Component } from 'react';

const InfoContext = React.createContext();

// Provider
export default class InfoProvider extends Component {
    render() {
        return (
            
            <InfoContext.Provider value="Hello this is the ressource">
                {this.props.children}
            </InfoContext.Provider>
        );
    }
}

// Consumer
const InfoConsumer=InfoContext.Consumer;

export {InfoConsumer, InfoProvider};
