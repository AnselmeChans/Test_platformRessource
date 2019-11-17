import React, { Component } from 'react';
import { placeInfo, reviews, detailInfo, news} from '../data'

const InfoContext = React.createContext();

// Provider
export default class InfoProvider extends Component {

    state = {
        info: placeInfo, 
        reviews: reviews, 
        detailInfo: detailInfo, 
        new: news
    }

    render() {
        return (
            
            <InfoContext.Provider value={{
                info: this.state.placeInfo, 
                reviews: this.state.reviews, 
                detailInfo: this.state.detailInfo, 
                new: this.state.news

            }}>
                {this.props.children}
            </InfoContext.Provider>
        );
    }
}

// Consumer
const InfoConsumer=InfoContext.Consumer;

export {InfoConsumer, InfoProvider};
