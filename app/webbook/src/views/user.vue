<template>
    <el-container>
        <el-header height="60px" >
            <p  align = center>
                用户界面
            </p>
        </el-header>
        <el-container>
            <el-aside width="400px" style="background-color: rgb(238, 241, 246)">  
                <el-menu >
                    <el-menu-item index="1"  >
                        <el-button round v-on:click.native="im_index=1" icon="el-icon-s-unfold">  
                            借书记录
                        </el-button>
                    </el-menu-item>
                    <el-menu-item index="2" >
                        <el-button round v-on:click.native="im_index=2" @click.native="test" icon="el-icon-s-unfold">  
                            未还书籍
                        </el-button>
                    </el-menu-item> 
                    <el-menu-item index="3"  >
                        <el-button round @click.native="im_index=3" icon="el-icon-s-unfold" >  
                           欠款记录
                        </el-button>
                    </el-menu-item>
                </el-menu>
            </el-aside>
        
            <el-main>
                <el-table :data="tableData" v-if="im_index == 1 || im_index==2" >
                    <el-table-column prop="ISBN" label="日期书号" width="140">
                    </el-table-column>
                    <el-table-column prop="name" label="书名" width="120">
                    </el-table-column>
                    <el-table-column prop="due_date" label="应还日期">
                    </el-table-column>
                    <el-table-column fixed="right" label="操 作" width="100">
                        <template slot-scope="scope">
                            <el-button  type="text" size="small"  @click="handleClick(scope.row)">还 书</el-button>
                            <el-button type="text" size="small"   @click=" this.$refs.flag = true" >续 借</el-button>
                            <el-dialog title="提示" :visible.sync="this.$refs.flag" width="30%"  center>
                                <span>是否续借</span>
                                <span slot="footer" class="dialog-footer">
                                    <el-button @click="this.$refs.flag= false">取 消</el-button>
                                    <el-button type="primary"   @click="this.$refs.flag = false">确 定</el-button>
                                </span>
                            </el-dialog>
                        </template>
                    </el-table-column>  
                </el-table>
                <el-table v-else>
                    <el-table-column prop="reason" label="欠款原因" width="140">
                    </el-table-column>
                     <el-table-column prop="price" label="欠款金额" width="120">
                    </el-table-column>
                    <el-table-column prop="date" label="欠款日期" width="120">
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
        <div>
            <p>
                {{ im_index }}
            </p>
        </div>
    </el-container>

</template>


<script>
export default ({
    name :"user" ,
    setup() {
        
    },
    data () {
        const item =  {
            ISBN: 'a516160',
            name: 'python_web',
            due_date: '2021-6-10',
        };
        return {
        tableData: Array(20).fill(item) ,
        im_index : 1 ,
        centerDialogVisible: false ,
      }
    } ,
    method :{
        test :function() {
           console.log(im_index)
        },
        handleClick :function(row ) {
            console.log(row)   
        },
        handleClose:function(done) {
            this.$confirm('确认关闭？')
            .then(_ => {
                done();
            })
            .catch(_ => {});
      }
    }

  
})
</script>
