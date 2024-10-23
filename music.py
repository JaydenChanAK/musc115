import pygame
import time

def print_program():
    print("""
===============================================
Welcome to the 8-Bit Symphony!
Program:
    1) Moonlight Sonata...............Beethoven
    2) Spring - The Four Seasons........Vivaldi
    3) Sinfonia from Cantata BMV 35........Bach
    4) Symphony No. 40. 4th Mbt..........Mozart
    5) Minute Waltz......................Chopin
===============================================
Type 's' in the pop-up window during a piece to stop it early.
Press ctrl-c in the terminal to exit.
""")

def display_art(art, delay):
    for image in art:
        print(image)
        time.sleep(delay)
        print("\033[H\033[J", end="")

def play_music(title, art):
    file_path = f"songlist/{title}"
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        display_art(art, 0.5)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    print("\nSong stopped.\n")
                    return
    
def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Press 's' here to stop song.")
    
    program_list = ["moonlight_sonata.mp3", "spring.mp3", "sinfonia.mp3", 
               "symphony_no40.mp3", "minute_waltz.mp3"]
    ascii_art = [
    """
             ;I;              
             +It.             
             +II+             
             +III;            
             +IIII;           
             iIIIII;          
             titIIII;         
             I;.iIIII;        
            .I;  =IIII;       
            .I;   ;IIII:      
            .I;    :tIIt      
            .I;     .tII=     
            .I;      :III     
            :I;       +II;    
            :I;       .II=    
            :I:        iIi    
            :I.        ;Ii    
            ;I.        =I;    
            ;I.        tt     
            +I        ;I;     
            +I       ;I;      
            tI      ;I;       
     :;itIIIII     +t:        
   ;tIIIIIIIII   :t;          
 .tIIIIIIIIIIi  ;i.           
.tIIIIIIIIIII;.;:             
;IIIIIIIIIII;                 
;IIIIIIIIIt;                  
 ;tIIIIt+;                    
   ....
    """,
"""





             ;I;              
             +It.             
             +II+             
             +III;            
             +IIII;           
             iIIIII;          
             titIIII;         
             I;.iIIII;        
            .I;  =IIII;       
            .I;   ;IIII:      
            .I;    :tIIt      
            .I;     .tII=     
            .I;      :III     
            :I;       +II;    
            :I;       .II=    
            :I:        iIi    
            :I.        ;Ii    
            ;I.        =I;    
            ;I.        tt     
            +I        ;I;     
            +I       ;I;      
            tI      ;I;       
     :;itIIIII     +t:        
   ;tIIIIIIIII   :t;          
 .tIIIIIIIIIIi  ;i.           
.tIIIIIIIIIII;.;:             
;IIIIIIIIIII;                 
;IIIIIIIIIt;                  
 ;tIIIIt+;                    
   ....
    """
    ]
    
    print_program()
    command = input("Type any number to play that piece, p to view the program, or type q to quit: ")
    
    while command != 'q':
        try:
            if command == 'p':
                print_program()
                command = input("Type any number to play that piece, p to view the program, or type q to quit: ")
                continue
            index = int(command) - 1
            if 0 <= index < len(program_list):
                play_music(program_list[index], ascii_art)
            else:
                print("Invalid input, try again.\n")
        except ValueError:
            print("Invalid input, try again.\n")
    
        command = input("Type any number to play that piece, p to view the program, or type q to quit: ")
        print() # newline
        
    print("We hope you enjoyed the performance!")
    pygame.quit()
   
if __name__ == '__main__':
    main()