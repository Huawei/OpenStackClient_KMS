1	POST /v1.0/{project_id}/kms/create-key	Create Key
2	POST /v1.0/{project_id}/kms/list-keys	List Keys
3	POST /v1.0/{project_id}/kms/describe-key	Describe Key
4	POST /v1.0/{project_id}/kms/disable-key	Disable Key
5	POST /v1.0/{project_id}/kms/enable-key	Enable Key

6	POST /v1.0/{project_id}/kms/gen-random	Generate Random


7	POST /v1.0/{project_id}/kms/create-datakey	Create DataKey
8	POST /v1.0/{project_id}/kms/create-datakey-without-plaintext	Create DataKey Without Plaintext
9	POST /v1.0/{project_id}/kms/encrypt-datakey	EnCrypt DataKey
10	POST /v1.0/{project_id}/kms/decrypt-datakey	Decrypt DataKey

11	POST /v1.0/{project_id}/kms/schedule-key-deletion	Schedule Key Deletion
12	POST /v1.0/{project_id}/kms/cancel-key-deletion	Cancel Key Deletion


  keypair create  Create new public or private key for server ssh access
  keypair delete  Delete public or private key(s)
  keypair list   List key fingerprints
  keypair show   Display key details
