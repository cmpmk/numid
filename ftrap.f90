program trapezoidal
  implicit none
  real :: a, b
  integer, parameter :: n = 50
  real :: h
  integer :: k
  real, dimension(n) :: x, res

  a = 1
  b = 10
  
  h = (b-a)/n 
  res = 0.5*(x(a) + x(b))

!  do k = 1, n
!     res = h*x(a + k*h)
!     res = 
!  end do
  write (*,*) "why"
  write (*,*) h !, res
end program trapezoidal






  !interface
  !   function f(x)
  !     real(SP), dimension(:), intent(in) :: x
  !     real(SP), dimension(size(x)) :: f
  !   end function f

  ! end interface

  
