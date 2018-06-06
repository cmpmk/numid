subroutine quad(a,b,c)
  implicit none
  real :: x1, x2
  real :: a, b, c
  real :: disc

  read (*,*) a, b, c
  disc = sqrt(b**2 - 4*a*c)

  x1 = (-b + disc)/2*a

  x2 = (-b - disc)/2*a

  write (*,*) 'x1 = ', x1
  write (*,*) 'x2 = ', x2
end subroutine quad





  
