


INSERT INTO #comp: 
    if self.is_root: #>> 
        self.ref('root')
    #<<
    if not self.is_root: #>> 
        self.ref('users')
    #<<
    #end (username, email, password) 
VALUES (
        '#comp: self.ref(self.username) #end', 
        '#comp: self.ref(self.email) #end',
        '#comp: self.ref(self.password) #end'
);
