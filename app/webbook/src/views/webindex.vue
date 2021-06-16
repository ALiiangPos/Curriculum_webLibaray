<template>
    <el-container>
        <el-header>
            <el-header>
                <el-row>
                    <el-col :span="24">
                        <div class="grid-content bg-purple-dark">
                            Library 
                        </div>
                    </el-col>
                </el-row>
            </el-header>
            <el-menu default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect"
                                                background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                <el-menu-item index="1" @click="button_1">图书检索</el-menu-item>
                <el-menu-item index="2" @click="button_2">图书馆信息</el-menu-item>
                <el-menu-item index="3" @click="button_3">信息和公告</el-menu-item>
                <el-menu-item index="4" @click="button_4">反馈中心</el-menu-item>
            </el-menu>
        </el-header>
        <div>
            <br>
            <br>
        </div>
        <el-main>
            <el-container>
                <el-aside width="800px">
                    <div id = "messaggearea">
                        <el-container style="150px">
                            <div>
                                <p>
                                 text area 
                                </p>
                            </div>
                        </el-container>
                    </div>
                    <div class="block">
                        <el-carousel height="350px">
                        <el-carousel-item v-for="item in 4" :key="item">
                            <h3 class="small">{{ item }}</h3>
                        </el-carousel-item>
                        </el-carousel>
                    </div>
                </el-aside>
                <el-container>
                    <el-main>
                        <div>
                            <el-container style="height:500px">
                                <div>
                                    <p>
                                        hello text 
                                    </p>
                                </div>
                            </el-container>
                        </div>
                    </el-main>
                    <el-footer>
                        <div class="block">
                            <el-pagination
                                layout="prev, pager, next"  
                                :total="50">
                            </el-pagination>
                        </div>
                    </el-footer>
                </el-container>
            </el-container>
        </el-main>
        <el-footer>
            <p id = "">
                @ Disigned  with Element-UI
            </p>
        </el-footer>
    </el-container>
</template>


<style scoped>
    -bg-purple-dark{
        background: #99a9bf;
    }
     .el-aside {
    background-color: #F6F8FB;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
    .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
  #messaggearea {
      background-color: #e3e8ee;
  }
</style>



<script>
export default ({
    name :"webindex" ,
    data :{
        tests:[
            {
            key :'第一条公告',
            value:"www.baidu.com"
            },
            {
                key:'第一条公告' ,
                value :'https://blog.csdn.net/qq_52170993?spm=1011.2124.3001.5343',
            },
            {
                key:'第一条公告',
                value :'https://leetcode-cn.com/problemset/all/'
            }
        ],
    },
    props: {
        msg : String
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }

})
</script>
