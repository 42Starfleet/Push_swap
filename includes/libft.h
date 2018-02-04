/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ztisnes <ztisnes@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/09/21 21:47:24 by ztisnes           #+#    #+#             */
/*   Updated: 2018/02/03 17:35:01 by ztisnes          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*TODO: Reorganize and make libft better and efficient
**		Consider in creating obstack header
**		restructure lists and other ADT
**		Create unique files for stacks, queues, and binary trees
*/

#ifndef LIBFT_H
# define LIBFT_H

# include <unistd.h>
# include <stdlib.h>
# include <string.h>

/*
** Linked List structure
*/

typedef struct		s_list
{
	void			*content;
	size_t			content_size;
	struct s_list	*next;
}					t_list;

t_stack				*init_stack(void);
void				push_stack(t_stack *stack, void *content);
void				*pop_stack(t_stack *stack);
void				*peek(t_stack *stack);
int					isEmpty_stack(t_stack *stack);
#endif
