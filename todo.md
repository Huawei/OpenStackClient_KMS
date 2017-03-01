
r1、预期：openstack kms key create --alias keyalias --realm eu-de
--description desc --policy policy --usage usage --type keytype
--sequence 919c82d4-8046-4722-9094-35c3c6524cff
r1、预期：openstack kms key enable --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
--sequence 919c82d4-8046-4722-9094-35c3c6524cff
r1、预期：openstack kms key disable --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
--sequence 919c82d4-8046-4722-9094-35c3c6524cff
r1、预期：openstack kms key schedule deletion
--key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f --pending-days 7
--sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms key cancel deletion
--key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
--sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms key list --limit 2 --marker 0
--sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms key describe --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
--sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms random generate --random-data-length 512
--sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms datakey create --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f --encryption-context context --datakey-length 512 --sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms datakey create
--without-plain-text --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
--encryption-context context --datakey-length 512
--sequence 919c82d4-8046-4722-9094-35c3c6524cff

r1、预期：openstack kms datakey encrypt --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f --encryption-context context --plain-text plaintext --datakey-plain-length 64 --sequence 919c82d4-8046-4722-9094-35c3c6524cff
r1、预期：openstack kms datakey decrypt --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f --encryption-context context --cipher-text ciphertext --datakey-cipher-length 64 --sequence 919c82d4-8046-4722-9094-35c3c6524cff
4、--encryption-context context 与aws保持一致，使用--encryption-context ，context为json字符串，且值为key-value对。
5、参数已根据建议修改为：--alias keyalias --realm eu-de --description desc --policy policy --usage usage --type keytype