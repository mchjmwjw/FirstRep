
=> ES6箭头语法：参数 => 返回值

    // ES5  
    (function (h) {  
      return h(App);  
    });  
      
    // ES6  
    h => h(App); 

----------------------------------

render: h => h(App)  

	//ES5      
	render: function(createElement) {
		return createElement(App);
	}
	
	render(h){
		return h(app);
	}

将 h 作为 createElement 的别名是 Vue 生态系统中的一个通用惯例，实际上也是 JSX 所要求的，如果在作用域中 h 失去作用， 在应用中会触发报错。

-----------------------------------

`Promise`对象代表一个异步操作，有三种状态：

​	`Pending`（进行中）

​	`Resolved`（已完成，又称 Fulfilled）

​	`Rejected`（已失败）



Promise.prototype.then()

```
getJson('/posts.json').then(function(json) {
  return json.post;
}).then(function(post) {
  //....
})
// 上述代码，使用then方法，依次执行两个回调函数，第一个回调函数的返回值作为第二个函数的参数
```



```
getJSON("/post/1.json").then(function(post) {
  return getJSON(post.commentURL);
}).then(function funcA(comments) {
  console.log("Resolved: ", comments);
}, function funcB(err){
  console.log("Rejected: ", err);
});
//上面代码中，第一个then方法指定的回调函数，返回的是另一个Promise对象。
//这时，第二个then方法指定的回调函数，就会等待这个新的Promise对象状态发生变化。
//如果变为Resolved，就调用funcA，如果状态变为Rejected，就调用funcB。
//简化写法
getJSON('/post/1.json').then(
  post => getJSON(post.commentURL)
).then(
  comments => console.log("Resolved: ", comments);
  err => console.log("Rejected: ", err);
);
```

对象展开运算符 ...