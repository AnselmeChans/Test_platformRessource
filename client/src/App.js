
// --------------------------- Import packages -----------------------------------


import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Provider, connect } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import {auth} from "./actions";
import ressourcesApp from "./reducers";
import thunk from "redux-thunk";
import {BrowserRouter, Switch, Route, Redirect} from 'react-router-dom';





// --------------------------- Import Components -----------------------------------


import Navbar from './components/layouts/Navbar';
import Footer from './components/layouts/Footer';
import Home from './components/pages/Home';
import Contact from './components/pages/Contact';
import Ressources from './components/pages/Ressources';
import NotFoundPage from './components/pages/NotFoundPage';
import Register from './components/pages/register';
import Login from './components/pages/Login';


// ------------------------------- PLATFORM RESSOURCES APP --------------------------------------

let store = createStore(ressourcesApp, applyMiddleware(thunk));


class RootContainerComponent extends Component {

  componentDidMount() {
      this.props.loadUser();
  }

  PrivateRoute = ({component: ChildComponent, ...rest}) => {
      return <Route {...rest} render={props => {
          if (this.props.auth.isLoading) {
              return <em>Loading...</em>;
          } else if (!this.props.auth.isAuthenticated) {
              return <Redirect to="/login" />;
          } else {
              return <ChildComponent {...props} />
          }
      }} />
  }

  render() {
      let {PrivateRoute} = this;
      return (
          <BrowserRouter>
              <Switch>
                  <PrivateRoute exact path="/" component={Ressources} />
                  <Route exact path="/register" component={Register} />
                  <Route exact path="/login" component={Login} />
                  <Route path="/contact" component={Contact}></Route>
                  <Route Component={NotFoundPage}></Route>
              </Switch>
          </BrowserRouter>
      );
  }
}



const mapStateToProps = state => {
  return {
      auth: state.auth,
  }
}

const mapDispatchToProps = dispatch => {
  return {
      loadUser: () => {
          return dispatch(auth.loadUser());
      }
  }
}


let RootContainer = connect(mapStateToProps, mapDispatchToProps)(RootContainerComponent);


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar></Navbar>
        <Switch>
          <Provider store={store}>
            <RootContainer />
          </Provider>
        </Switch>
      </BrowserRouter>
      
      <Footer></Footer>
    </div>
  );
}

export default App;








