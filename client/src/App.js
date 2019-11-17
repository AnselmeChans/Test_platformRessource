import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/layouts/Navbar';
import Footer from './components/layouts/Footer';
import Home from './components/pages/Home';
import Contact from './components/pages/Contact';
import Ressources from './components/pages/Ressources';
import NotFoundPage from './components/pages/NotFoundPage';
import {BrowserRouter, Switch, Route} from 'react-router-dom';



function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar></Navbar>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route path="/room" component={Ressources}></Route>
          <Route path="/contact" component={Contact}></Route>
          <Route component={NotFoundPage}></Route>
        </Switch>
      </BrowserRouter>
      
      <Footer></Footer>
    </div>
  );
}

export default App;
