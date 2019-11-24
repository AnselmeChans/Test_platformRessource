import React, { Component } from 'react'
import { Button, Card } from 'react-bootstrap';


export default class CardsRessources extends Component {
    render() {
        return (
            <Card style={{ width: '18rem' }}>
                <Card.Img variant="top" src="holder.js/100px180" />
                <Card.Body>
                    <Card.Title> tile Restaurant </Card.Title>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card's content.
                    </Card.Text>
                    <Button variant="primary">Detail</Button>
                    <Button variant="primary">Geolocalisation</Button>
                </Card.Body>
            </Card>
        )
    }
}
