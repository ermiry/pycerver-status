# PyCerver Status Service

### Development

```
sudo docker run \
  -it \
  --name status --rm \
  -p 5000:5000 \
  -v /home/ermiry/Documents/ermiry/Projects/pycerver-status:/home/status \
  -e RUNTIME=development \
  -e PORT=5000 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  ermiry/pycerver-status:development /bin/bash
```

### Test

```
sudo docker run \
  -it \
  --name status --rm \
  -p 5000:5000 \
  -e RUNTIME=test \
  -e PORT=5000 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  ermiry/pycerver-status:test /bin/bash
```

### Production

```
sudo docker run \
  -d \
  --name status --rm \
  -p 5000:5000 \
  -e RUNTIME=production \
  -e PORT=5000 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  ermiry/pycerver-status:production
```

### Main

#### GET /api/status
**Access:** Public \
**Description:** Status service top level route \
**Returns:**
  - 200 on success

#### GET api/status/version
**Access:** Public \
**Description:** Returns status service current version \
**Returns:**
  - 200 and version's json on success
