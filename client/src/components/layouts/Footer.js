import React, { Component } from 'react'
import styled from 'styled-components';

export default class Footer extends Component {
    render() {
        return (
            <FooterContainer className="main-footer">
                <div className="footer-middle">
                    <div className="container">
                        <div className="row">
                            <div class="col-md-3 col-sm-6">
                                <h4>lorem ipsum</h4>
                                <ul className="list-unstyled">
                                    <li><a href="/">lorem ipsum</a></li>
                                    <li><a href="/">lorem ipsum</a></li>
                                    
                                </ul>
                            </div>

                            <div class="col-md-3 col-sm-6">
                                <h4>lorem ipsum</h4>
                                <ul className="list-unstyled">
                                    <li><a href="/">lorem ipsum</a></li>
                                    <li><a href="/">lorem ipsum</a></li>
                                </ul>
                            </div>

                            <div class="col-md-3 col-sm-6">
                                <h4>lorem ipsum</h4>
                                <ul className="list-unstyled">
                                    <li><a href="/">lorem ipsum</a></li>
                                    <li><a href="/">lorem ipsum</a></li>
                                </ul>
                            </div> 
                        </div>
                        <div className="footer-bottom">
                            <p className="text-xs-center">
                                &copy; {new Date().getFullYear()} Platform Room Reservation App - All Right Reserved
                            </p>
                        </div>
                    </div>
                </div>
            </FooterContainer>
        )
    }
}

const FooterContainer = styled.footer `
    .footer-middle{
        background: var(--mainDark);
        padding-top: 3rem;
        color: var(--mainWhite);
    }

    .footer-bottom{
        padding-top: 3rem;
        padding-bottom: 2rem;
    }
`;
