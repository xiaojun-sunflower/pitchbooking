import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN": 'xiaojun.eu.auth0.com',
    "ALGORITHMS": ['RS256'],
    "API_AUDIENCE": 'pitchbooking'
}

token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh0RTIwbm1FQWtuZnNTQ1l2NVpRQiJ9.eyJpc3MiOiJodHRwczovL3hpYW9qdW4uZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNGQwMzY1NTkzNTgwMDA2NzU0YTM1YyIsImF1ZCI6InBpdGNoYm9va2luZyIsImlhdCI6MTYwMDUwOTY3MCwiZXhwIjoxNjAwNTgxNjcwLCJhenAiOiJzT0hZSTZwYTBUZG11MWVYTnpxOVliNkNTUkhRcHUxcyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnBpdGNoIiwiZ2V0OnBpdGNoIiwicGF0Y2g6cGl0Y2giLCJwb3N0OmJvb2tpbmciLCJwb3N0OnBpdGNoZXMiXX0.EtL6BkyBEDXCieuTZESlNPBhElAQ6Em6ZnZBU1VyApE9_fqoN8k1JmiuE9cbwO6Kc7I6Yl17AaPIe0YCBnD9rm7bXNUOu0oyozaEsQfCT5EQgKTYYaEkN5hZdWIntNtMpxs_7ZVVggsU9bWAo_q2NA1qCnNJOk9D-l_Mbql-ulkNasNUpxz4IywZN8CUhckfEzQND9XvVJBbdckC_vAvRxDJvMqTR01Glq_iFJ5teEie_Z4KL5uC7J5_dW4ZOm7Az-AWVffgqPgBGAZcX7P85tJEASa7LwduMJXZkGBatBaAVV7kGfoJ6_7mFTFJTaQ05huzODh6IpELLA6Bu9TtVQ"
