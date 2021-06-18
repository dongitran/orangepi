class StatusDevice{
  constructor(id, version, status){
    this.id = id;
    this.version = version;
    this.status = status;
  }
  IsDevice(id){
    if(this.id != id){
      return true;
    }
    return false;
  }
  IsNeedUpdate(version){
    if(this.version != version){
      return true;
    }
    return false;
  }
}

module.exports = StatusDevice;
