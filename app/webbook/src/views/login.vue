<template>
    <div class="loginpage" >
        <div >
            <div class="rectangle">
                <div >
                    <br>
                    <br>
                    <div text-align="center" style="color:#000000">
                        用户登陆
                    </div>
                    <br>
                    <el-form label-position="labelPosition" label-width="80px" >
                        <el-form-item label="账号">
                            <el-input  placeholder="账号" style="width = 50px"></el-input>
                        </el-form-item>
                        <el-form-item label="密码">
                            <el-input type="password"  placeholder="密码" style="width = 50px"></el-input>
                        </el-form-item>
                        <el-form-item label="活动形式">
                            <el-input ></el-input> 
                        </el-form-item>
                        <el-button type="primary" round @click="button_1" style="width = 50px">登陆</el-button>
                    </el-form>
                    <br>
                    <br>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default ({
    name :"login" ,
    data :{
        
    } ,
    method :{
        button_1() {
            axios({
                method:'get',
                url:'user.json'
            }).then(function(res){
                console.log(res.data.name);
            }) ;
        }
    }
    
})
</script>
    
<style scoped>
    .loginpage {
        background: url("../assets/login.jpg")  center center no-repeat ;
        width: 1920px;
        height: 1080px;
        overflow:hidden;
        background-size: 100% 100%;
    } 

    .rectangle{
    width:30%;
    height:30%;
    margin-top: 300px  ;
	margin-left: 500px ;
    text-align: center;
    color: #92C5EA;
    background:rgb(255, 255,255);
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    border-top-left-radius: 10px;
    border-top-right-radius:10px ;
}
 .el-input {
      width: 400px ;
    }
</style>
