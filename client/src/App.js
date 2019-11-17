import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/layouts/Navbar';
import Footer from './components/layouts/Footer';

function App() {
  return (
    <div className="App">
      <Navbar></Navbar>
      <Footer></Footer>
    </div>
  );
}

export default App;
