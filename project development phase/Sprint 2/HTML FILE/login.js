function validate()
{
    var username=document.getElementById("username").Value;
    var password=document.getElementById("password").Value;
    if(username=="pooja"&&password=="miii")
    {
        alert("login succesfully");
        return true;
    }
    else
    {
        document.getElementById("username").disabled=true;
        document.getElementById("password").disabled=true; 
        return false;
    }
    
}


{
    document.getElementById("email").value="";
    document.getElementById("pwd1").value="";
}