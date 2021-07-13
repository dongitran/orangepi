class StatusDevice{
  constructor(id, type, version, status, timeUpdate){
    this.id = id;
    this.type = type;
    this.version = version;
    this.status = status;
    this.timeUpdate = timeUpdate;
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
  IsOffline(time){
    if((time - this.timeUpdate) > 20000){
      return true;
    }
    return false;
  }
}

module.exports = StatusDevice;

