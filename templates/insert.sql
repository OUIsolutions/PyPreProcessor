


INSERT INTO #comp: 
    if self.root_user: #>> 
        self.ref('root')
    #<<
    if not self.root_user: #>> 
        self.ref('users')
    #<<
    #end (username, email, password) 
VALUES (
        '#comp: self.ref(self.username) #end', 
        '#comp: self.ref(self.email) #end',
        '#comp: self.ref(self.password) #end'
);
