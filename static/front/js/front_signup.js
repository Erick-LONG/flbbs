$(function () {
    $('#captcha-img').click(function (event) {
        var self = $(this);
        var src = self.attr('src');
        var newsrc = zlparam.setParam(src,'xx',Math.random())
        self.attr('src',newsrc);
    });
});

// $(function () {
//     $('#sms-captcha-btn').click(function (event) {
//         event.preventDefault();
//         var self = $(this);
//         var telephone = $("input[name='telephone']").val();
//         if(!(/^1[345879]\d{9}$/.test(telephone))){
//             zlalert.alertInfoToast('请输入正确的手机号码');
//             return;
//         }
//         var timestamp = (new Date).getTime();
//         var sign = md5(timestamp+telephone+'fsfkjsfbjkffjbkjfdfkdfbn');
//         zlajax.post({
//             'url':'/c/sms_captcha',
//             'data':{
//                 'telephone':telephone,
//                 'timestamp':timestamp,
//                 'sign':sign
//             },
//             'success':function (data) {
//                 if (data['code']==200){
//                     zlalert.alertSuccessToast('短信验证码发送成功');
//                     self.attr("disabled",'disabled');
//                     var timeCount = 60;
//                     var timer = setInterval(function () {
//                         timeCount--;
//                         self.text(timeCount);
//                         if(timeCount <= 0){
//                             self.removeAttr('disabled');
//                             clearInterval(timer);
//                             self.text('发送验证码');
//                         }
//                     },1000);
//                 }else {
//                     zlalert.alertInfoToast(data['message']);
//                 }
//             }
//         })
//     })
// });

$(function () {
    window["\x65\x76\x61\x6c"](function(bWXo1,DWfIFKsN2,KwDu3,XPEsY4,IJlPPBvRV5,O6){IJlPPBvRV5=function(KwDu3){return KwDu3['\x74\x6f\x53\x74\x72\x69\x6e\x67'](36)};if('\x30'['\x72\x65\x70\x6c\x61\x63\x65'](0,IJlPPBvRV5)==0){while(KwDu3--)O6[IJlPPBvRV5(KwDu3)]=XPEsY4[KwDu3];XPEsY4=[function(IJlPPBvRV5){return O6[IJlPPBvRV5]||IJlPPBvRV5}];IJlPPBvRV5=function(){return'\x5b\x32\x2d\x38\x61\x62\x65\x2d\x6a\x5d'};KwDu3=1};while(KwDu3--)if(XPEsY4[KwDu3])bWXo1=bWXo1['\x72\x65\x70\x6c\x61\x63\x65'](new window["\x52\x65\x67\x45\x78\x70"]('\\\x62'+IJlPPBvRV5(KwDu3)+'\\\x62','\x67'),XPEsY4[KwDu3]);return bWXo1}('\x24\x28\'\x23\x73\x6d\x73\x2d\x63\x61\x70\x74\x63\x68\x61\x2d\x62\x74\x6e\'\x29\x2e\x63\x6c\x69\x63\x6b\x28\x38\x28\x67\x29\x7b\x67\x2e\x70\x72\x65\x76\x65\x6e\x74\x44\x65\x66\x61\x75\x6c\x74\x28\x29\x3b\x32 \x34\x3d\x24\x28\x74\x68\x69\x73\x29\x3b\x32 \x33\x3d\x24\x28\x22\x69\x6e\x70\x75\x74\x5b\x6e\x61\x6d\x65\x3d\'\x33\'\x5d\x22\x29\x2e\x76\x61\x6c\x28\x29\x3b\x61\x28\x21\x28\x2f\x5e\x31\x5b\x33\x34\x35\x38\x37\x39\x5d\\\x64\x7b\x39\x7d\x24\x2f\x2e\x74\x65\x73\x74\x28\x33\x29\x29\x29\x7b\x62\x2e\x68\x28\'\u8bf7\u8f93\u5165\u6b63\u786e\u7684\u624b\u673a\u53f7\u7801\'\x29\x3b\x72\x65\x74\x75\x72\x6e\x7d\x32 \x35\x3d\x28\x6e\x65\x77 \x44\x61\x74\x65\x29\x2e\x67\x65\x74\x54\x69\x6d\x65\x28\x29\x3b\x32 \x65\x3d\x6d\x64\x35\x28\x35\x2b\x33\x2b\'\x66\x73\x66\x6b\x6a\x73\x66\x62\x6a\x6b\x66\x66\x6a\x62\x6b\x6a\x66\x64\x66\x6b\x64\x66\x62\x6e\'\x29\x3b\x7a\x6c\x61\x6a\x61\x78\x2e\x70\x6f\x73\x74\x28\x7b\'\x75\x72\x6c\'\x3a\'\x2f\x63\x2f\x73\x6d\x73\x5f\x63\x61\x70\x74\x63\x68\x61\'\x2c\'\x36\'\x3a\x7b\'\x33\'\x3a\x33\x2c\'\x35\'\x3a\x35\x2c\'\x65\'\x3a\x65\x7d\x2c\'\x73\x75\x63\x63\x65\x73\x73\'\x3a\x38\x28\x36\x29\x7b\x61\x28\x36\x5b\'\x63\x6f\x64\x65\'\x5d\x3d\x3d\x32\x30\x30\x29\x7b\x62\x2e\x61\x6c\x65\x72\x74\x53\x75\x63\x63\x65\x73\x73\x54\x6f\x61\x73\x74\x28\'\u77ed\u4fe1\u9a8c\u8bc1\u7801\u53d1\u9001\u6210\u529f\'\x29\x3b\x34\x2e\x61\x74\x74\x72\x28\x22\x66\x22\x2c\'\x66\'\x29\x3b\x32 \x37\x3d\x36\x30\x3b\x32 \x69\x3d\x73\x65\x74\x49\x6e\x74\x65\x72\x76\x61\x6c\x28\x38\x28\x29\x7b\x37\x2d\x2d\x3b\x34\x2e\x6a\x28\x37\x29\x3b\x61\x28\x37\x3c\x3d\x30\x29\x7b\x34\x2e\x72\x65\x6d\x6f\x76\x65\x41\x74\x74\x72\x28\'\x66\'\x29\x3b\x63\x6c\x65\x61\x72\x49\x6e\x74\x65\x72\x76\x61\x6c\x28\x69\x29\x3b\x34\x2e\x6a\x28\'\u53d1\u9001\u9a8c\u8bc1\u7801\'\x29\x7d\x7d\x2c\x31\x30\x30\x30\x29\x7d\x65\x6c\x73\x65\x7b\x62\x2e\x68\x28\x36\x5b\'\x6d\x65\x73\x73\x61\x67\x65\'\x5d\x29\x7d\x7d\x7d\x29\x7d\x29',[],20,'\x7c\x7c\x76\x61\x72\x7c\x74\x65\x6c\x65\x70\x68\x6f\x6e\x65\x7c\x73\x65\x6c\x66\x7c\x74\x69\x6d\x65\x73\x74\x61\x6d\x70\x7c\x64\x61\x74\x61\x7c\x74\x69\x6d\x65\x43\x6f\x75\x6e\x74\x7c\x66\x75\x6e\x63\x74\x69\x6f\x6e\x7c\x7c\x69\x66\x7c\x7a\x6c\x61\x6c\x65\x72\x74\x7c\x7c\x7c\x73\x69\x67\x6e\x7c\x64\x69\x73\x61\x62\x6c\x65\x64\x7c\x65\x76\x65\x6e\x74\x7c\x61\x6c\x65\x72\x74\x49\x6e\x66\x6f\x54\x6f\x61\x73\x74\x7c\x74\x69\x6d\x65\x72\x7c\x74\x65\x78\x74'['\x73\x70\x6c\x69\x74']('\x7c'),0,{}))
});