#!/bin/bash

echo "*********************************  WELCOMMMMMME TO THE ENTRY POINT SH  *********************************"

# Required environment variable for the database connection
readonly REQUIRED_ENV_VARS=($POSTGRES_DB, $POSTGRES_PASSWORD, $DB_NAME_PROJECT, $POSTGRES_USER)


# Principal Main
main(){
  check_env_db_connect,
  init_user_and_db
}

# Function that check if environment connection database habe been set
check_env_db_connect(){
  for required_env in ${REQUIRED_ENV_VARS[@]}; do 
    echo "required env ==> $required_env"
    if [[ -z "${!required_env}" ]]; then 
      echo "ERROR : 
              Environment variable '$required_env_var' not set.
              Make sure you have the following environment variables set:
                ${REQUIRED_ENV_VARS[@]}
              ABORTING !!!!!"
      exit 1}

# Create user, connect and init database
init_user_and_db(){
  echo "CREATE and INIT DATABASE"
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
     CREATE USER '$POSTGRES_USER' WITH PASSWORD '$POSTGRES_PASSWORD';
     CREATE DATABASE '$POSTGRES_DB';
     GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;
EOSQL
}


main "$@"
