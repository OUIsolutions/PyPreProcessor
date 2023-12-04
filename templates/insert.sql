


INSERT INTO 
#comp: if self.is_root: #>>  #end
    root 
#<<
#comp:if not self.is_root: #>> #end 
     users 
#<<
(username, email, password) 
VALUES (
        '#comp: self.ref(self.username) #end', 
        '#comp: self.ref(self.email) #end',
        '#comp: self.ref(self.password) #end'
);
