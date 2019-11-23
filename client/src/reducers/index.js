import { combineReducers } from 'redux';

import auth from "./auth";


const ressourcesApp = combineReducers({
    auth,
})

export default ressourcesApp;